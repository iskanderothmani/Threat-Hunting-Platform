"""Run documented hunt hypotheses against offline event dictionaries."""
HUNTS=(
 {"id":"HUNT-001","name":"Authentication failures","field":"event_type","equals":"auth_failure"},
 {"id":"HUNT-002","name":"PowerShell process event","field":"process_name","equals":"powershell.exe"},
 {"id":"HUNT-003","name":"Privilege change event","field":"event_type","equals":"privilege_change"},
)
def run_hunt(events,hunt):
 if not isinstance(events,list) or not isinstance(hunt,dict): raise ValueError("Events and hunt must be structured data")
 field=hunt.get("field"); expected=hunt.get("equals")
 if not isinstance(field,str) or not isinstance(expected,str): raise ValueError("Hunt needs string field and equals values")
 matches=[event for event in events if isinstance(event,dict) and str(event.get(field,"")).casefold()==expected.casefold()]
 return {"hunt_id":hunt.get("id","CUSTOM"),"name":hunt.get("name","Custom hunt"),"match_count":len(matches),"matches":matches}
if __name__=="__main__":
 demo=[{"event_type":"auth_failure","user":"demo"},{"process_name":"powershell.exe","host":"lab-host"}]
 for hunt in HUNTS: print(run_hunt(demo,hunt))
