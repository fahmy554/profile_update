import traceback

try:
    from main_app import get_input,update_profile,log_time
except KeyboardInterrupt:
    print('User Stop')

except Exception as e:
    print('Error', e)
    traceback.print_exc()
