# Postmortem Incident Report

This guide details how to write an effective Incident Report, often referred to as a Postmortem. This report structure aligns closely with the guidelines used by Google engineers for incident documentation. The report is composed of five key sections: Issue Summary, Timeline, Root Cause Analysis, Resolution and Recovery, and Corrective and Preventative Measures. Each section plays a crucial role in ensuring a comprehensive understanding of the incident and preventing future occurrences. Below is an expanded explanation of each section.

### Issue Summary

- **Brief Overview:** Provide a concise overview of the incident in approximately five sentences. This should summarize the key details of the incident without going into excessive detail.
- **Duration:** Clearly state the start and end times of the incident, including the date and the specific time zone (e.g., UTC, PST, etc.). This helps establish the timeframe during which the impact occurred.
- **Impact:** Describe the impact of the incident on users and systems. For instance, specify how many users were affected, the nature of the issue (e.g., 500 errors on user requests), and the peak impact (e.g., 100% of requests failing).
- **Root Cause:** Conclude this section with a brief mention of the root cause, setting the stage for more detailed analysis later in the report.

### Timeline

- **Time Zone:** Start by specifying the time zone in which all times will be reported. This ensures consistency and clarity for anyone reading the report.
- **Incident Duration:** Detail the entire duration of the outage or incident, from the moment it began until full service restoration.
- **Key Events:**
  - **Incident Start:** Specify the exact time the incident began.
  - **Notification:** Record the time at which staff or relevant teams were first alerted to the issue.
  - **Actions and Events:** Document each significant action taken, event that occurred, or change made in response to the incident. Include timestamps for each entry to track the sequence of events accurately.
  - **Service Restoration:** Note the time at which the service was fully restored and normal operations resumed.

### Root Cause Analysis

- **In-Depth Explanation:** Provide a detailed and thorough explanation of what caused the incident. This section should explore the technical aspects, including any software bugs, configuration errors, infrastructure failures, or human errors that led to the issue.
- **Transparency:** Be honest and direct in this section. Avoid minimizing the severity of the issue or omitting relevant details. A transparent analysis is critical for learning and improving.

### Resolution and Recovery

- **Detailed Actions:** Describe in detail the steps taken to resolve the issue and restore service. Include all actions performed, whether they were successful or not, to provide a complete picture of the response efforts.
- **Timestamps:** Include the specific times at which key actions were taken, correlating them with the timeline to offer a clear understanding of the sequence and impact of each decision.
- **Challenges Encountered:** Mention any difficulties or challenges faced during the resolution process, such as unforeseen complications, delays, or the need for additional resources.

### Corrective and Preventative Measures

- **Preventative Steps:** List specific actions that will be taken to prevent a similar incident from occurring in the future. These could include changes to processes, infrastructure improvements, code updates, or enhanced monitoring.
- **Continuous Improvement:** Reflect on the incident response process and identify areas for improvement. Consider what could be done better next time, whether in terms of communication, response speed, or technical solutions.
- **Action Items:** Clearly outline any action items assigned to specific teams or individuals, with deadlines for implementation. This ensures accountability and follow-through on the proposed measures. 

This structure ensures that the incident is thoroughly analyzed, and the learnings are effectively captured, leading to improved resilience and faster response times in future incidents.