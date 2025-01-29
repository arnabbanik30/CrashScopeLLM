import ollama

from run_report import append_and_print_report


def get_crash_summary(dump, package_name):
    messages = [{
        'role' : 'user',
        'content' : f'analyze the logs and stack trace below. tell me why the {package_name} app crashed.' + dump
    }]
    append_and_print_report("Analyzing Stack Trace and generating summary")

    response = ollama.chat(
        model = "errorqwen",
        messages=messages
    )

    assistant_message = response['message']['content']

    append_and_print_report("AI Summary: ")
    append_and_print_report(assistant_message)

    return assistant_message