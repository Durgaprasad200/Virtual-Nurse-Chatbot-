import datetime
import json

def log_action(user_input, steps, result):
    log = {
        "input": user_input,
        "steps": steps,
        "result": result,
        "time": str(datetime.datetime.now())
    }
    with open("audit_log.json", "a") as f:
        f.write(json.dumps(log) + "\n")

def safe_ai_call(model, prompt):
    for _ in range(3):
        try:
            res = model.generate_content(prompt)
            return res.text if res and res.text else "No response"
        except:
            pass
    return "AI service unavailable. Try again later."

def process_agent(nurse, user_input):
    steps = []
    try:
        steps.append("Understand user query")

        if "medication" in user_input.lower():
            steps.append("Tool call: get_medications")
            data = nurse.get_medications()
            steps.append("AI reasoning")
            response = safe_ai_call(nurse.model, str(data))

        elif "appointment" in user_input.lower():
            steps.append("Tool call: get_appointments")
            data = nurse.get_appointments()
            steps.append("AI reasoning")
            response = safe_ai_call(nurse.model, str(data))

        elif "vital" in user_input.lower():
            steps.append("Tool call: get_vitals")
            data = nurse.get_vital_signs()
            steps.append("AI reasoning")
            response = safe_ai_call(nurse.model, str(data))

        else:
            steps.append("Direct AI response")
            response = safe_ai_call(nurse.model, user_input)

        log_action(user_input, steps, response)

        return {"response": response, "steps": steps}

    except Exception as e:
        return {"response": "System error", "steps": steps, "error": str(e)}
