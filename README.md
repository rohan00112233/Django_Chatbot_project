## Current Status: Deployed with a Known Issue

* **Live URL:** http://18.234.46.163
* **Status:** The application is successfully deployed and running on AWS EC2. The frontend loads correctly.
* **Known Issue:** There is a persistent runtime bug where the bot does not return a response to the user on the live server. This is likely due to a final configuration issue or a silent timeout when communicating with the AI API in the production environment.

## Debugging and Problems Solved

During this project, numerous deployment and configuration challenges were diagnosed and fixed, including:
* Correcting Django's `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` for production.
* Resolving Gunicorn worker timeouts with the `--timeout` flag.
* Fixing server-side `[Errno 98] Address already in use` port conflicts by managing server processes.
* Diagnosing and fixing `sudo` environment path and variable issues.
* Resolving multiple Python `SyntaxError` and `ModuleNotFoundError` issues.