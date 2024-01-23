# Metrics API for side projects

This flask API provides a way to retrieve metrics for my side projects, currently used in shield badge generation.

## Usage

- Get project metrics:

  ```
  GET /projects/usercount?name=project_name`
  ```

  Response JSON:

  ```json
  {
    "user_count": "123"
  }
  ```

## Deployment

This API is deployed on fly.io, and can be accessed at https://project-metrics-flask.fly.dev/

To deploy, run

```bash
flyctl deploy
```

To view logs, run

```bash
flyctl logs
```
