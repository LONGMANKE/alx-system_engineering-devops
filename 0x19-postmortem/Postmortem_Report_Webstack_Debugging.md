# Postmortem Report

## Database Connection Outage

<p align="center">
<img src="https://raw.githubusercontent.com/MitaliSengupta/holberton-system_engineering-devops/master/0x19-postmortem/image.gif" width=100% height=100% />
</p>

### Incident report for [504 error / Site Outage](https://github.com/MitaliSengupta/holberton-system_engineering-devops/tree/master/0x17-web_stack_debugging_3)

#### Summary

## Issue Summary

- **Duration:** The outage lasted for 3 hours, from 9:00 AM to 12:00 PM (GMT+3) on August 10, 2024.
- **Impact:** The outage affected the company's primary web application, resulting in downtime for all users. Approximately 100% of active users (around 5,000) were unable to access the service, experiencing errors such as "500 Internal Server Error" and "Unable to connect to the database."
- **Root Cause:** The root cause was a misconfigured connection pool on the database server, which led to the exhaustion of available connections, causing the web application to fail in establishing new database connections.

## Timeline

- **9:00 AM:** Issue detected through automated monitoring alerts indicating an increase in the error rate and a drop in successful HTTP requests.
- **9:05 AM:** Engineers on-call noticed the alerts and began investigating the application logs, which showed repeated database connection errors.
- **9:20 AM:** Initial assumption was that the database server was down. The database server logs were checked, showing no signs of downtime, but the number of active connections was unusually high.
- **9:40 AM:** Engineers restarted the web servers, suspecting a possible memory leak or resource exhaustion, but the issue persisted.
- **10:00 AM:** The incident was escalated to the database administration team, who started analyzing the database performance and configuration.
- **10:20 AM:** Misleading investigation paths included checking for network issues and possible DDoS attacks, but these were ruled out after analyzing network traffic and firewall logs.
- **10:40 AM:** The database team identified that the connection pool was configured with a maximum of 50 connections, which was insufficient for peak traffic loads.
- **11:00 AM:** The connection pool configuration was adjusted, increasing the maximum connections to 200 and optimizing the idle connection timeout settings.
- **11:30 AM:** The web application was restarted, and the error rate gradually decreased as new connections were established successfully.
- **12:00 PM:** The issue was resolved, and normal service was restored. A post-incident meeting was scheduled to review the event and discuss corrective actions.

## Root Cause and Resolution

**Root Cause:**  
The outage was caused by an improperly configured connection pool in the web application's database connection settings. The connection pool had a maximum limit of 50 connections, which was sufficient under normal conditions but inadequate during peak usage. As the number of users increased, the application exhausted all available connections, leading to errors when trying to establish new connections.

**Resolution:**  
The resolution involved increasing the maximum connection pool size from 50 to 200, allowing more simultaneous database connections to be established. Additionally, idle connection timeout settings were optimized to ensure that unused connections were released promptly, freeing up resources for new connections. After making these changes, the web application was restarted, and normal operation resumed without any further connection issues.

## Corrective and Preventative Measures

**Improvements:**
1. **Capacity Planning:** Implement regular reviews of connection pool configurations based on user traffic patterns and peak usage forecasts.
2. **Enhanced Monitoring:** Set up more granular monitoring for database connection pool usage, with alerts for thresholds approaching maximum capacity.
3. **Database Optimization:** Review and optimize database queries to reduce connection time, ensuring efficient use of resources.
4. **Incident Response Training:** Conduct training sessions for the engineering team on database troubleshooting and connection pool management to improve response times in future incidents.

**Tasks:**
1. **Update Connection Pool Settings:** Review and adjust connection pool settings across all environments (development, staging, production) to align with the current traffic loads.
2. **Implement Monitoring Alerts:** Add monitoring for connection pool usage, with specific alerts for when usage exceeds 80% of the configured capacity.
3. **Perform Load Testing:** Conduct load testing on the web application to ensure the connection pool can handle peak traffic scenarios.
4. **Schedule Regular Configuration Reviews:** Set up quarterly reviews of database and application server configurations to anticipate future scaling needs.

By implementing these corrective measures, we aim to prevent similar incidents from occurring in the future, ensuring higher availability and reliability of our services.
