# PayPilotLabs Framework

The base that every PayPilotLabs product runs on: it holds your data, logins, screens, email and background work in one place.

## What it does

- Keeps your records (customers, tickets, invoices and so on) in a database and lets each product define its own record types.
- Handles users, roles and permissions, so each person sees only what they should.
- Gives every product the same admin screens (the "desk" at `/desk`), the login page and the customer portal.
- Sends and receives email, and keeps a queue so nothing is lost if a mail server is down.
- Runs background jobs and scheduled tasks, such as reminders and reports.
- Builds lists, reports, dashboards and printable documents (PDF) from your records.
- Offers a REST API and webhooks so other systems can read and write your data.
- Supports notifications, assignments, comments, file attachments, import and export, and many languages.

## How it helps your business

- One login and one permission system across all your PayPilotLabs products.
- Your data stays in your own database, on your own server.
- Routine work (reminders, emails, reports) runs by itself in the background.
- Other tools can connect through the API, so you do not retype data.
- Every change is tracked, so you can see who did what and when.

## How it fits with other PayPilotLabs products

This is the foundation. PayPilotLabs Helpdesk, CRM, ERP, HRMS and Insights all run on top of it, together with companion apps such as paypilotlabs-telephony (phone calls) and paypilotlabs-payments (payment gateways). You do not install it alone: each product's `docker/build.sh` builds one image with this framework and that product inside.

## Run it

This is a companion app: it is installed alongside a PayPilotLabs product by that product's `docker/build.sh`. See the product repo's README.

Support and requests: https://paypilotlabs.com/roadmap/

## Licence

MIT. See [LICENSE](LICENSE). Based on open-source work by others; see [NOTICE.md](NOTICE.md) for credits.
