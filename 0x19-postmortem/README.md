# Postmortem Report: Black Friday Website Outage

## Issue Summary

- **Duration of Outage:** From 10:00 AM to 1:00 PM (SAST+2)
- **Impact:** The e-commerce website experienced a severe outage, causing unresponsiveness for approximately three hours. Users were unable to complete purchases, and it affected 100% of visitors during the outage.
- **Root Cause:** The root cause of the outage was inadequate server capacity planning for high-traffic events.

## Timeline

- **Issue Detected:** November 25, 10:00 AM (SAST+2)
- **Detection Method:** The issue was detected when monitoring systems triggered alerts due to a spike in server resource utilization. 
- **Actions Taken:**
    - The technical team immediately investigated the issue, identifying it as a server overload.
    - They scaled up server resources and made adjustments to handle the increased traffic.
- **Misleading Paths:**
    - Initially, there were assumptions of a potential DDoS attack, but further investigation ruled out any malicious activity.
    - There was a brief exploration into a database issue, but it was quickly ruled out as well.
- **Escalation:** The incident was escalated to the entire technical team, including the DevOps, infrastructure, and database teams.
- **Resolution:** The incident was resolved by 1:00 PM (SAST+2) after scaling up server resources to meet the demand.

## Root Cause and Resolution

- **Root Cause Explanation:** The root cause was a failure in server capacity planning. The website's servers were not adequately provisioned to handle the surge in traffic on Black Friday, leading to a resource overload. This resulted in unresponsiveness and, ultimately, the outage.
- **Resolution Details:** To address the issue, the technical team scaled up server resources in real-time. Additionally, they decided to implement proactive load testing to ensure the system's capacity meets high-traffic demands in the future.

## Corrective and Preventative Measures

- **Improvements/Fixes:**
    - Enhance server capacity planning to accommodate traffic spikes during high-traffic events.
    - Improve monitoring and alerting systems to detect resource utilization issues earlier.
    - Develop a playbook for handling similar incidents in the future.
- **Tasks:**
    - Conduct regular load testing to ensure the system can handle anticipated traffic spikes.
    - Implement automatic scaling for critical resources during high-traffic periods.
    - Review and optimize server resource allocation to prevent overloads.

By implementing these measures, we aim to prevent similar incidents and provide a better shopping experience for our users during peak traffic times.

---

This fictional postmortem report provides a comprehensive overview of the incident, including its impact, timeline, root cause, resolution, and corrective/preventative measures. 

