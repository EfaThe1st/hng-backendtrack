from flask import Flask, request, jsonify
import datetime
import pytz
import os

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def get_info():
        # Get query parameters
        slack_name = request.args.get('Eunice_Ofem', 'Eunice_Ofem')
        track = request.args.get('backend', 'backend')

        # Get current day of the week
        current_day = datetime.datetime.now(pytz.utc).strftime("%A")

        # Get current UTC time with validation of +/-2 minutes
        utc_time = datetime.datetime.now(pytz.utc)
        valid_utc_time = utc_time + datetime.timedelta(hours=0, minutes=-2)

        # Get GitHub URL of the file being run
        github_file_url = "https://github.com/EfaThe1st/hng-backendtrack/blob/master/script.py"


        # Get GitHub URL of the repo
        github_repo_url = "https://github.com/EfaThe1st/hng-backendtrack"

        #Get Status Code
        status_code = 200

                                                                                                                                       # Prepare the response data
        data = {                                                                                                              
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": valid_utc_time.strftime("%Y-%m-%dT%H:%M:%S %Z"),
            "track": track,
            "github_file_url": github_file_url,
            "github_repo_url": github_repo_url,
            "status_code": status_code
        }

        # Return the response in JSON format with a success status code
        return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
                    





