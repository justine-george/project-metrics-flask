# Metrics Flask API

This Flask API is designed to retrieve user metrics for my projects. It is utilized on the jgeorge.dev homepage (at build-time) and for generating shield badges.

## Usage

### Get User Count for Chrome Extensions

```
GET /extensions/{extensionId}/usercount
```

Note: Replace `{extensionId}` with the actual ID of the Chrome extension you're inquiring about.

#### Response JSON:

```json
{
  "user_count": "123"
}
```

## Deployment

This API is currently deployed on fly.io and can be accessed at:

https://project-metrics-flask.fly.dev/

To deploy the application, execute:

```bash
flyctl deploy
```

To view the application logs, run:

```bash
flyctl logs
```
