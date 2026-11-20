# Shopping UI Automation

A beginner-friendly Selenium and pytest project that checks shopping flows on the public demo storefront at `https://sauce-demo.myshopify.com/`. The project uses the Page Object Model, meaningful Allure test labels, and failure screenshots to make results easier to understand.

## What is covered

- Add products and verify cart counts.
- Open the cart and check product names and quantities.
- Check product and cart totals after quantity changes.
- Capture browser screenshots and failure details in Allure when a test fails.

Customer-registration tests are intentionally marked **skipped**: they are placeholders and do not yet exercise the registration page. They are labeled in the reports so they cannot be mistaken for passing coverage.

## Run locally

### Requirements

- Python 3.12+
- Google Chrome
- Java 17+ and Node.js 20+ to build and open the Allure HTML report

In PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -v --alluredir=reports/allure-results --clean-alluredir --html=reports/pytest-report.html --self-contained-html
```

The tests run headlessly in Chrome. Set `$env:HEADLESS = "false"` to watch the browser while testing. To test another compatible storefront, set `$env:BASE_URL` before running pytest.

Build and open the Allure dashboard locally:

```powershell
npx.cmd --yes allure-commandline@2.34.1 generate reports/allure-results --clean -o reports/allure-report
npx.cmd --yes allure-commandline@2.34.1 open reports/allure-report
```

The standalone pytest HTML report is `reports/pytest-report.html`. Allure's raw results and generated dashboard are written under `reports/`; failure screenshots and logs are added when a test fails.

## Run with Docker Compose

Docker Desktop with Docker Compose is the only local prerequisite:

```powershell
docker compose run --build --rm ui-tests
```

The container includes Chromium and runs it headlessly. The `reports/` directory is mounted from the repository so the Allure results and pytest HTML report remain available on your machine after the container exits. For a different test URL:

```powershell
$env:BASE_URL = "https://your-test-store.example/"
docker compose run --build --rm ui-tests
```

Generate and view the Allure dashboard using the local commands above.

## GitHub Actions

The workflow in `.github/workflows/ui-tests.yml` builds the Docker image, runs the Selenium suite, generates the Allure HTML dashboard and pytest HTML report, and uploads reports as a 30-day workflow artifact. On the repository's default branch, it also publishes the Allure dashboard to GitHub Pages.

To enable the hosted dashboard, open **Settings → Pages** in the repository and select **GitHub Actions** as the build and deployment source. The workflow needs `pages: write` and `id-token: write` permissions, which are declared in the workflow. Reports remain available as workflow artifacts even when Pages is not enabled.

The tests use a live external demo storefront, so their results depend on that site being reachable and retaining the selectors and behavior the tests expect.
