from django.test import TestCase
from django.contrib.auth.models import User, Group, Permission
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from .models import Youth, Offence, SupportProgram
from .services import get_all_youth_records, generate_support_recommendations


class YouthModelTest(TestCase):
    def setUp(self):
        self.youth = Youth.objects.create(
            name="Test Youth",
            age=16,
            gender="Male",
            background_notes="Requires support and monitoring.",
            school_status="Attending",
            family_support_level="Medium"
        )

    def test_youth_string_representation(self):
        self.assertEqual(str(self.youth), "Test Youth")

    def test_youth_can_have_offence_record(self):
        offence = Offence.objects.create(
            youth=self.youth,
            offence_type="Theft",
            severity="SERIOUS",
            date_reported=timezone.now().date(),
            notes="Serious offence recorded."
        )

        self.assertEqual(offence.youth, self.youth)
        self.assertEqual(offence.severity, "SERIOUS")


class SupportRecommendationServiceTest(TestCase):
    def setUp(self):
        self.youth = Youth.objects.create(
            name="Recommendation Test Youth",
            age=17,
            gender="Male",
            background_notes="Dropped out of school and needs intervention.",
            school_status="Dropped Out",
            family_support_level="Low"
        )

        self.offence = Offence.objects.create(
            youth=self.youth,
            offence_type="Assault",
            severity="SERIOUS",
            date_reported=timezone.now().date(),
            notes="Requires counselling and rehabilitation."
        )

        self.counselling_program = SupportProgram.objects.create(
            name="Counselling Support Program",
            description="Provides behavioural and emotional support.",
            program_type="Counselling"
        )

        self.rehabilitation_program = SupportProgram.objects.create(
            name="Rehabilitation Program",
            description="Provides structured rehabilitation support.",
            program_type="Rehabilitation"
        )

    def test_get_all_youth_records_returns_youths(self):
        youths = get_all_youth_records()

        self.assertEqual(youths.count(), 1)
        self.assertEqual(youths.first().name, "Recommendation Test Youth")

    def test_generate_support_recommendations_returns_expected_structure(self):
        result = generate_support_recommendations(self.youth)

        self.assertIn("programs", result)
        self.assertIn("reasons", result)
        self.assertIn("latest_offence", result)

    def test_generate_support_recommendations_includes_latest_offence(self):
        result = generate_support_recommendations(self.youth)

        self.assertEqual(result["latest_offence"], self.offence)
        self.assertTrue(
            any("Latest offence severity" in reason for reason in result["reasons"])
        )


class RoleBasedAccessTest(TestCase):
    def setUp(self):
        self.youth = Youth.objects.create(
            name="Access Test Youth",
            age=15,
            gender="Female",
            background_notes="Test access control record.",
            school_status="Attending",
            family_support_level="Medium"
        )

        Offence.objects.create(
            youth=self.youth,
            offence_type="School misconduct",
            severity="MINOR",
            date_reported=timezone.now().date(),
            notes="Minor incident for access testing."
        )

        SupportProgram.objects.create(
            name="Youth Mentoring Program",
            description="Provides mentoring support.",
            program_type="Mentoring"
        )

        self.volunteer_user = User.objects.create_user(
            username="volunteer",
            password="Testpass123"
        )

        self.case_worker_user = User.objects.create_user(
            username="caseworker",
            password="Testpass123"
        )

        self.volunteer_group = Group.objects.create(name="Volunteer")
        self.case_worker_group = Group.objects.create(name="Case Worker")

        youth_content_type = ContentType.objects.get_for_model(Youth)
        support_program_content_type = ContentType.objects.get_for_model(SupportProgram)
        offence_content_type = ContentType.objects.get_for_model(Offence)

        view_youth = Permission.objects.get(
            codename="view_youth",
            content_type=youth_content_type
        )

        change_youth = Permission.objects.get(
            codename="change_youth",
            content_type=youth_content_type
        )

        view_support_program = Permission.objects.get(
            codename="view_supportprogram",
            content_type=support_program_content_type
        )

        view_offence = Permission.objects.get(
            codename="view_offence",
            content_type=offence_content_type
        )

        self.volunteer_group.permissions.add(
            view_youth,
            view_offence,
            view_support_program
        )

        self.case_worker_group.permissions.add(
            view_youth,
            change_youth,
            view_offence,
            view_support_program
        )

        self.volunteer_user.groups.add(self.volunteer_group)
        self.case_worker_user.groups.add(self.case_worker_group)

    def test_anonymous_user_redirected_from_home_page(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 302)

    def test_volunteer_can_access_youth_records(self):
        self.client.login(username="volunteer", password="Testpass123")

        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Access Test Youth")

    def test_case_worker_can_access_youth_records(self):
        self.client.login(username="caseworker", password="Testpass123")

        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Access Test Youth")

    def test_case_worker_can_access_recommendations(self):
        self.client.login(username="caseworker", password="Testpass123")

        response = self.client.get(
            reverse("recommendations", args=[self.youth.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Support Recommendations")

    def test_volunteer_cannot_access_recommendations(self):
        self.client.login(username="volunteer", password="Testpass123")

        response = self.client.get(
            reverse("recommendations", args=[self.youth.id])
        )

        self.assertNotEqual(response.status_code, 200)