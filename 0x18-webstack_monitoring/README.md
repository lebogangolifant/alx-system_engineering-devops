# 0x18. Webstack monitoring

This project focuses on web stack monitoring, using Datadog as the monitoring tool. It covers the setup, configuration, and monitoring of system and application metrics for effective management and optimization of your web servers.

## Dependencies

- Ubuntu 16.04 LTS
- Bash scripts should pass `Shellcheck` (version 0.3.7) without any errors.


## Table of Contents
- [Task 0: Datadog Setup](#task-0-datadog-setup)
- [Task 1: System Metrics Monitoring](#task-1-system-metrics-monitoring)
- [Task 2: Dashboard Creation](#task-2-dashboard-creation)

## Task 0: Datadog Setup

### Description
In this task, we set up Datadog, a monitoring service, for system and application monitoring. We sign up for a Datadog account, configure it to monitor system metrics, and install the Datadog agent on a specific server.

### Instructions
- Sign up for a Datadog account on the US website.
- Set the region to US1.
- Install the Datadog agent on the web-01 server.
- Create an application key and copy the API and application keys.
- Update the Intranet user profile with the keys.
- Ensure that the server web-01 is visible in Datadog.

## Task 1: System Metrics Monitoring

### Description
This task involves setting up monitors in Datadog to check the number of read and write requests issued to a device per second. These monitors will help in monitoring and alerting for system metrics.

### Instructions
- Set up a monitor to check the number of read requests issued to the device per second.
- Set up a monitor to check the number of write requests issued to the device per second.

## Task 2: Dashboard Creation

### Description
In this task, we create a Datadog dashboard and add various widgets to visualize different metrics. The dashboard provides a visual representation of system and application performance.

### Instructions
- Create a new dashboard.
- Add at least 4 widgets to the dashboard to monitor different metrics.
- Retrieve the dashboard ID using Datadog's API.

## Files
- `2-setup_datadog`: Contains the dashboard ID for Task 2.

## Conclusion
This project aims to enhance monitoring and alerting capabilities using Datadog for effective system and application management. It ensures that critical metrics are continuously monitored and visualized, providing insights for better decision-making and problem-solving.
