# Pi Agent - reporting the health of your Raspberry Pi via GPT

- collect system information via:
   - mpstat -o JSON
   - df -h
   - free -h
   - pgrep -f octoprint
   - vcgencmd measure_temp
 - ask GPT what to make of this and wether to raise an alarm
 - send notification via Pushover



<img src="https://github.com/remcoder/pi-agent/assets/461650/604f182c-b838-4b75-bb16-8824d6e74fd0" width=300 />

```mermaid
flowchart TD 
A[Start] --> B[Collect System Metrics]
B --> D[Analyze Report with GPT-3]
D --> F{Is Alert Needed?}
F -->|True|G[Send Notification]
F -->|False|H[Log Status & Exit] 
G --> I[End] 
H --> I
```
