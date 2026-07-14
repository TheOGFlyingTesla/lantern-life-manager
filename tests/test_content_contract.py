from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "lantern-life-manager"


class ContentContractTests(unittest.TestCase):
    def test_global_untrusted_content_rule_loads_before_routing(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8").casefold()
        core = text.split("## route the request", 1)[0]

        for required in (
            "external content",
            "untrusted data",
            "disclose private data",
            "bypass approval",
        ):
            self.assertIn(required, core)

    def test_skill_routes_every_core_workflow(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8").casefold()

        for required in (
            "guided onboarding",
            "domain status",
            "work request",
            "recover",
            "capability",
            "model",
        ):
            self.assertIn(required, text)

    def test_skill_description_is_trigger_only(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn(
            "description: Use when someone wants ongoing help coordinating",
            text,
        )

    def test_domain_status_is_freshness_aware(self):
        text = (
            SKILL / "assets" / "templates" / "STATUS.md"
        ).read_text(encoding="utf-8")

        for required in ("Last verified", "Review after", "Confidence"):
            self.assertIn(required, text)

    def test_domain_status_matches_approved_compact_schema(self):
        text = (
            SKILL / "assets" / "templates" / "STATUS.md"
        ).read_text(encoding="utf-8")
        fields = [
            line
            for line in text.splitlines()
            if line.startswith("- ")
        ]

        self.assertEqual(
            fields,
            [
                "- State: not reviewed",
                "- Outcome: unknown",
                "- Current situation: unknown",
                "- Completed: none confirmed",
                "- Important dates: unknown",
                "- Blockers or decisions: unknown",
                "- Next action: complete first domain check-in",
                "- Confidence: low",
                "- Last verified: never",
                "- Review after: first use",
                "- No personal information has been collected yet.",
            ],
        )

    def test_dashboard_example_matches_header_width(self):
        lines = (
            SKILL / "assets" / "templates" / "DASHBOARD.md"
        ).read_text(encoding="utf-8").splitlines()
        table = [line for line in lines if line.startswith("|")]

        self.assertGreaterEqual(len(table), 3)
        width = table[0].count("|")
        self.assertTrue(all(line.count("|") == width for line in table))

    def test_architecture_is_one_local_project_with_folder_scoped_domains(self):
        text = (SKILL / "references" / "architecture.md").read_text(
            encoding="utf-8"
        ).casefold()

        for required in (
            "local-first",
            "one local project",
            "lantern root",
            "domains/",
            "status.md",
            "inbox.md",
            "on demand",
            "do not create cloud chatgpt projects",
            "no git repository",
            "optional backup",
        ):
            self.assertIn(required, text)

    def test_local_starter_tree_is_complete(self):
        onboarding = (SKILL / "references" / "onboarding.md").read_text(
            encoding="utf-8"
        )
        for required in (
            "Lantern/",
            "AGENTS.md",
            "DASHBOARD.md",
            "Domains/",
            "Personal",
            "Career & Job Search",
            "Work, Internships & Volunteering",
            "School & Learning",
            "Appointments & Admin",
            "Health & Wellbeing",
            "Relationships & Community",
        ):
            self.assertIn(required, onboarding)

    def test_local_projects_boot_from_agents_files_and_domains_start_lazily(self):
        workspace = ROOT / "starter-workspace" / "Lantern"
        manager = (workspace / "AGENTS.md").read_text(encoding="utf-8").casefold()
        start = (workspace / "START_HERE.md").read_text(encoding="utf-8").casefold()
        domain = (workspace / "Domains" / "AGENTS.md").read_text(encoding="utf-8").casefold()

        self.assertIn("start lantern", start)
        self.assertIn("first genuine task", manager)
        self.assertIn("do not start a task in every domain", manager)
        self.assertIn("on demand", manager)
        self.assertIn("status.md", domain)
        self.assertIn("inbox.md", domain)

    def test_starter_workspace_contains_every_domain_and_durable_state(self):
        domains = ROOT / "starter-workspace" / "Lantern" / "Domains"
        for name in (
            "Personal",
            "Home",
            "Career & Job Search",
            "Work, Internships & Volunteering",
            "School & Learning",
            "Finances",
            "Appointments & Admin",
            "Health & Wellbeing",
            "Relationships & Community",
        ):
            folder = domains / name
            self.assertTrue(folder.is_dir(), name)
            for filename in ("START_HERE.md", "STATUS.md", "INBOX.md"):
                self.assertTrue((folder / filename).is_file(), f"{name}/{filename}")


    def test_safety_requires_exact_action_approval(self):
        text = (
            SKILL / "references" / "safety-and-permissions.md"
        ).read_text(encoding="utf-8").casefold()

        for required in (
            "exact target",
            "ask again",
            "untrusted content",
            "academic integrity",
            "fabricate",
        ):
            self.assertIn(required, text)

    def test_model_routing_is_cost_sensitive_without_overclaiming(self):
        routing = (SKILL / "references" / "model-routing.md").read_text(
            encoding="utf-8"
        ).casefold()

        for required in (
            "cost-sensitive personal-plan heuristic",
            "official default",
            "model and reasoning effort are separate",
            "normal ceiling",
            "parallel subagents",
            "not a smarter rung",
            "api cost charts",
            "plus allowance",
        ):
            self.assertIn(required, routing)

        for path in (ROOT / "starter-workspace" / "Lantern" / "AGENTS.md",):
            text = path.read_text(encoding="utf-8").casefold()
            self.assertIn("sol medium", text)
            self.assertIn("normal ceiling", text)
            self.assertIn("ultra", text)
            self.assertIn("parallel", text)

    def test_onboarding_builds_the_framework_before_domain_drilldown(self):
        onboarding = (SKILL / "references" / "onboarding.md").read_text(
            encoding="utf-8"
        ).casefold()
        manager = (ROOT / "starter-workspace" / "Lantern" / "AGENTS.md").read_text(encoding="utf-8").casefold()

        for text in (onboarding, manager):
            for required in (
                "framework-first",
                "four",
                "no more than three",
                "verify",
                "never answer",
            ):
                self.assertIn(required, text)

    def test_onboarding_uses_premade_framework_without_background_installer(self):
        onboarding = (SKILL / "references" / "onboarding.md").read_text(
            encoding="utf-8"
        ).casefold()
        manager = (ROOT / "starter-workspace" / "Lantern" / "AGENTS.md").read_text(encoding="utf-8").casefold()

        for text in (onboarding, manager):
            for required in (
                "already",
                "start lantern",
                "never claim",
                "verified",
                "do not start a task in every domain",
            ):
                self.assertIn(required, text)

    def test_onboarding_is_bounded_visual_and_skip_safe(self):
        onboarding = (SKILL / "references" / "onboarding.md").read_text(
            encoding="utf-8"
        ).casefold()
        manager = (ROOT / "starter-workspace" / "Lantern" / "AGENTS.md").read_text(encoding="utf-8").casefold()

        for text in (onboarding, manager):
            for required in (
                "step 1 of 4",
                "no more than three",
                "skipped means skipped",
                "life manager",
                "do not create cloud chatgpt projects",
                "start lantern",
                "status.md",
                "dashboard.md",
            ):
                self.assertIn(required, text)

        self.assertIn("questions remaining", onboarding)
        for domain in (
            "personal",
            "home",
            "career & job search",
            "work, internships & volunteering",
            "school & learning",
            "finances",
            "appointments & admin",
            "health & wellbeing",
            "relationships & community",
        ):
            self.assertIn(domain, onboarding)

    def test_onboarding_never_answers_for_the_user(self):
        onboarding = (SKILL / "references" / "onboarding.md").read_text(
            encoding="utf-8"
        ).casefold()
        manager = (ROOT / "starter-workspace" / "Lantern" / "AGENTS.md").read_text(encoding="utf-8").casefold()

        for text in (onboarding, manager):
            for required in (
                "never answer",
                "unknown",
                "never create both sides",
                "first genuine",
                "start_here.md",
            ):
                self.assertIn(required, text)

    def test_start_here_is_brief_and_has_one_activation_prompt(self):
        runtime = (ROOT / "starter-workspace" / "Lantern" / "START_HERE.md").read_text(encoding="utf-8")
        self.assertLessEqual(len(runtime.split()), 220)
        for required in (
            "Welcome to Lantern",
            "Start in three steps",
            "Start Lantern.",
            "only activation prompt",
        ):
            self.assertIn(required, runtime)

    def test_toolchain_guidance_separates_lantern_from_codex_prerequisites(self):
        capability = (SKILL / "references" / "capability-setup.md").read_text(
            encoding="utf-8"
        ).casefold()
        install = (ROOT / "docs" / "INSTALL.md").read_text(
            encoding="utf-8"
        ).casefold()

        for text in (capability, install):
            for required in (
                "lantern itself does not require git",
                "lantern itself does not require python",
                "codex",
                "apple developer tools",
                "xcode",
                "windows",
                "starter folder",
            ):
                self.assertIn(required, text)
        self.assertIn("bundled git", capability)

    def test_web_is_not_a_local_project_fallback(self):
        capability = (SKILL / "references" / "capability-setup.md").read_text(
            encoding="utf-8"
        ).casefold()
        troubleshooting = (ROOT / "docs" / "TROUBLESHOOTING.md").read_text(
            encoding="utf-8"
        ).casefold()

        self.assertIn("web version is not supported", capability)
        self.assertIn("do not fall back to a cloud chatgpt project", capability)
        self.assertIn("not supported on the web", troubleshooting)
        self.assertIn("one local project", troubleshooting)

    def test_runtime_archive_has_no_executable_files(self):
        forbidden = [
            path
            for path in SKILL.rglob("*")
            if path.is_file()
            and path.suffix.lower()
            not in {".md", ".yaml", ".yml", ".json", ".txt"}
        ]

        self.assertEqual(forbidden, [])

    def test_onboarding_checkpoint_and_recovery_are_durable(self):
        onboarding = (SKILL / "references" / "onboarding.md").read_text(
            encoding="utf-8"
        ).casefold()
        architecture = (SKILL / "references" / "architecture.md").read_text(
            encoding="utf-8"
        ).casefold()
        manager = (ROOT / "starter-workspace" / "Lantern" / "AGENTS.md").read_text(encoding="utf-8").casefold()

        for text in (onboarding, architecture, manager):
            self.assertIn("dashboard", text)
            self.assertIn("status.md", text)
        self.assertIn("recovery", architecture)

    def test_portable_export_is_a_runtime_workflow(self):
        skill = (SKILL / "SKILL.md").read_text(encoding="utf-8").casefold()
        architecture = (SKILL / "references" / "architecture.md").read_text(
            encoding="utf-8"
        ).casefold()
        manager = (ROOT / "starter-workspace" / "Lantern" / "AGENTS.md").read_text(encoding="utf-8").casefold()

        self.assertIn("export", skill)
        self.assertIn("references/architecture.md", skill)
        for text in (architecture, manager):
            self.assertIn("portable export", text)
            self.assertIn("dashboard", text)
            self.assertIn("status", text)


if __name__ == "__main__":
    unittest.main()
