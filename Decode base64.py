# import base64
#
# encoded_str = "PD9waHAgDQoNCi8qKg0KICogUGF1c2UgRGV2ZWxvcGVyIEFwcGxpY2F0aW9uIFNjcmlwdA0KICoNCiAqIFRoaXMgc2NyaXB0IHdpbGwgc3VibWl0IHlvdXIgcmVzdW1lIHRvIFBhdXNlJ3Mgc2VydmVyLg0KICogRml4IHRoZSBidWdzLCBmaWxsIGluIHRoZSBtaXNzaW5nIGNvZGUsIGFuZCBydW4gaXQgdG8gYXBwbHkgZm9yIHRoZSBqb2IuDQogKiBSZXF1aXJlcyB0aGUgQ1VSTCBtb2R1bGUgdG8gYmUgbG9hZGVkIGluIHlvdXIgUEhQIGluc3RhbGxhdGlvbi4NCiAqDQogKiBQbGVhc2UgTm90ZTogV2hpbGUgdGhpcyBzYW1wbGUgdGVzdCBpcyB3cml0dGVuIGluIHBocCwgd2UgZW5jb3VyYWdlIHlvdQ0KICogdG8gcmV3cml0ZSB0aGlzIGNvZGUgaW4gdGhlIGxhbmd1YWdlIG9mIHlvdXIgY2hvaWNlLCB3ZSBzaW1wbHkgcmVxdWlyZQ0KICogdGhlIHN1Ym1pc3Npb24gdG8gb3VyIHNlcnZlciB0byBtYXRjaCwgaG93IHlvdSBkbyBpdCBpcyBjb21wbGV0ZWx5IHVwDQogKiB0byB5b3UhDQogKg0KICogKGMpIDIwMTMgUGF1c2UgUHJvZHVjdGlvbnMNCiAqLw0KDQovLyBUaGlzIHNob3VsZCBwb2ludCB0byB0aGUgcmVzdW1lIGZpbGUgeW91IHdhbnQgdG8gc3VibWl0Lg0KLy8gTm90ZSB0aGlzIGlzIGEgcGF0aCB0byB0aGUgZmlsZSBvbiB5b3VyIGxvY2FsIGhhcmQgZHJpdmUsDQovLyBub3QgdGhlIGNvbnRlbnRzIG9mIHRoZSBmaWxlLiBGb3IgYmVzdCByZXN1bHRzLCB1c2UgUERGLA0KLy8gUlRGLCBET0MsIERPQ1gsIG9yIFRYVC4NCmRlZmluZSgnQVBQTElDQVRJT05fU0VSVkVSJywgJ2h0dHBzOi8vam9icy5wYXVzZS5jYS9zdWJtaXQucGhwJyk7DQoNCiRyZXN1bWVmaWxlID0gJy9wYXRoL3RvL3Jlc3VtZS5wZGYnOw0KDQovLyBZb3VyIGZ1bGwgbmFtZQ0KJG5hbWUgPSAnJzsNCg0KLy8gWW91ciBwaG9uZSBudW1iZXINCiRwaG9uZSA9ICcnOw0KDQovLyBZb3VyIGVtYWlsIGFkZHJlc3MNCiRlbWFpbCA9ICcnOw0KDQovLyBUaGUgbWVzc2FnZSB3ZSB3YW50IHRvIHNlbmQNCiRzdWJqZWN0ID0gJ015IGRldmVsb3BlciBhcHBsaWNhdGlvbic7DQoNCi8vIEFueSBhZGRpdGlvbmFsIG5vdGVzIHlvdSB3aXNoIHRvIGluY2x1ZGUNCi8vIEJvbnVzIHBvaW50cyBpZiB5b3UgZGlzY292ZXIgdGhlIHNlY3VyaXR5IGlzc3VlIHdpdGggdGhpcyBzY3JpcHQgb3INCi8vIGhhdmUgaWRlYXMgZm9yIGltcHJvdmVtZW50cyBhbmQgbm90ZSB0aGVtIGhlcmUuDQokbm90ZXMgPSAnJzsNCg0KLy8gUHJlcGFyZSB0aGUgcGF5bG9hZA0KJHZhcnMgPSBhcnJheSgNCgknbmFtZSc9JG5hbWUsDQoJJ3Bob25lJz0kcGhvbmUsDQoJJ2VtYWlsJz0kZW1haWwsDQoJJ3N1YmplY3QnPSRzdWJqZWN0LA0KCSdub3Rlcyc9JG5vdGVzLA0KCSd0aW1lJz10aW1lKCksDQopOw0KDQokY2ggPSBjdXJsX2luaXQoKTsNCmN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9VUkwsIEFQUExJQ0FUSU9OX1NFUlZFUik7DQpjdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfUE9TVEZJRUxEUywgJHZhcnMpOw0KY3VybF9zZXRvcHQoJGNoLCBDVVJMT1BUX1JFVFVSTlRSQU5TRkVSLCB0cnVlKTsNCmN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9TU0xfVkVSSUZZUEVFUiwgZmFsc2UpOw0KJHJlc3BvbnNlID0gY3VybF9leGVjKCRjaCk7DQoNCi8vZGVjb2RlIHRoZSBqc29uIGVuY29kZWQgcmVzcG9uc2UNCiRyZXNwb25zZVZhcnMgPSBkZWNvZGUoJHJlc3BvbnNlKTsNCg0KJHZhcnNbJ2FwcGxpY2F0aW9uLWlkJ10gPSAkcmVzcG9uc2VbJ2FwcGxpY2F0aW9uLWlkJ107DQoka2V5ID0gJHJlc3BvbnNlWydhcHBsaWNhdGlvbi1zZWNyZXQta2V5J107DQoNCg0KLy8gWW91IG11c3Qgd3JpdGUgdGhlIGNvZGUgdGhhdCBnZW5lcmF0ZXMgdGhlIHNpZ25hdHVyZSB0byBzaWduIHRoZSBhcHBsaWNhdGlvbg0KLy8gcmVxdWVzdC4gVGhpcyBpcyB2ZXJ5IHNpbWlsYXIgdG8gaG93IG90aGVyIHdlYiBzZXJ2aWNlcyBoYW5kbGUgc2lnbmF0dXJlcywNCi8vIHNvIHlvdSBtYXkgYmUgZmFtaWxpYXIgd2l0aCB0aGUgcHJvY2Vzcy4gSGVyZSdzIGhvdyB0byBkbyBpdDoNCg0KLy8gMSkgU29ydCB0aGUgJHZhcnMgYXJyYXkgYnkga2V5DQokdmFycyA9IGtzb3J0KCR2YXJzKTsNCg0KLy8gMikgQ29udmVydCB0aGUgc29ydGVkICR2YXJzIGFycmF5IHRvIGFuIGh0dHAgcXVlcnkgc3RyaW5nIChlZzogdmFyMT1hYmMmdmFyMj1kZWYpDQovLyBOb3RlIHRoaXMgc3RyaW5nIHNob3VsZCBub3QgYmUgcHJlcGVuZGVkIHdpdGggPywgaHR0cDovLywgb3IgYW55dGhpbmcgZWxzZSwNCi8vIGl0IHNob3VsZCBsb29rIGxpa2UgdGhlIGV4YW1wbGUgc3RyaW5nIGFib3ZlLi4uDQoNCi8vIDMpIENvbmNhdGVuYXRlIHRoZSBzdHJpbmcgZnJvbSBzdGVwIDIgYW5kICRrZXkgKHN0cmluZyB0aGVuICRrZXkpDQoNCi8vIDQpIEhhc2ggdGhlIHJlc3VsdGluZyBzdHJpbmcgZnJvbSBzdGVwIDMgdXNpbmcgU0hBMjU2LiBUaGlzIGlzIHlvdXIgc2lnbmF0dXJlLg0KJHNpZ25hdHVyZSA9ICdUaGlzIG11c3QgYmUgcmVwbGFjZWQgYnkgdGhlIGNvZGUgeW91IGdlbmVyYXRlIGluIHN0ZXBzIDEsMiwzLDQpJzsNCg0KLy8gNSkgQWRkIHRoZSBzaWduYXR1cmUgdG8gdGhlICR2YXJzIGFycmF5IGFzICdzaWcnIChkb25lIGZvciB5b3UsIGJlbG93KQ0KJHZhcnNbJ3NpZyddID0gJHNpZ25hdHVyZTsNCg0KLy8gQ2hlY2sgdGhhdCB0aGUgZmlsZSBleGlzdHMNCmlmICghZmlsZV9leGlzdHMoJHJlc3VtZWZpbGUpKSB7DQoJZGllKCdFUlJPUjogQ2Fubm90IGZpbmQgbG9jYWwgZmlsZSAnLiRyZXN1bWVmaWxlLiJcbiIpOw0KfQ0KDQovLyBBZGQgdGhlIGZpbGUgdG8gdXBsb2FkDQokdmFyc1sncmVzdW1lJ10gPSAnQCcuJHJlc3VtZWZpbGU7DQoNCi8vIEluY2x1ZGUgdGhpcyBzY3JpcHQgKHdlJ2QgbGlrZSB0byBzZWUgeW91ciB3b3JrIHBsZWFzZSEpDQokdmFyc1snc2NyaXB0J10gPSAnQCcuX19GSUxFX187DQoNCi8vIFBvc3QgdGhlIGRhdGEgdG8gUGF1c2UncyBzZXJ2ZXINCnByaW50ICJTdWJtaXR0aW5nIGFwcGxpY2F0aW9uLi4uXG4iOw0KJGNoID0gY3VybF9pbml0KCk7DQpjdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfVVJMLCBBUFBMSUNBVElPTl9TRVJWRVIpOw0KY3VybF9zZXRvcHQoJGNoLCBDVVJMT1BUX1BPU1RGSUVMRFMsICR2YXJzKTsNCmN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9SRVRVUk5UUkFOU0ZFUiwgMSk7DQpjdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfU1NMX1ZFUklGWVBFRVIsIGZhbHNlKTsNCiRyZXNwb25zZSA9IGN1cmxfZXhlYygkY2gpOw0KDQovLyBJZiB3ZSBnb3QgYmFjayAiT0siIHRoZW4gaXQgd2FzIHN1Ym1pdHRlZCBzdWNjZXNzZnVsbHkuDQovLyBPdGhlcndpc2UgaXQgc2hvdWxkIHRlbGwgdXMgd2hhdCB3ZW50IHdyb25nLg0KaWYgKCRyZXNwb25zZT09J09LJykgew0KCXByaW50ICJSZXN1bWUgc2VudCBzdWNjZXNzZnVsbHksIHRoYW5rIHlvdSBmb3IgYXBwbHlpbmchXG4iOw0KfQ0KZWxzZSB7DQoJcHJpbnQgIiRyZXNwb25zZVxuIjsNCn0NCg=="
#
# decodedCode = base64.b64decode(encoded_str)
# decoded_str = decodedCode.decode('utf-8')
#
# print(decoded_str)
#
#
# // This should point to the resume file you want to submit.
# // Note this is a path to the file on your local hard drive,
# // not the contents of the file. For best results, use PDF,
# // RTF, DOC, DOCX, or TXT.
# define('APPLICATION_SERVER', 'https://jobs.pause.ca/submit.php');
#
# $resumefile = '/path/to/resume.pdf';
#
# // Your full name
# $name = '';
#
# // Your phone number
# $phone = '';
#
# // Your email address
# $email = '';
#
# // The message we want to send
# $subject = 'My developer application';
#
# // Any additional notes you wish to include
# // Bonus points if you discover the security issue with this script or
# // have ideas for improvements and note them here.
# $notes = '';
#
# // Prepare the payload
# $vars = array(
# 	'name'=$name,
# 	'phone'=$phone,
# 	'email'=$email,
# 	'subject'=$subject,
# 	'notes'=$notes,
# 	'time'=time(),
# );
#
# $ch = curl_init();
# curl_setopt($ch, CURLOPT_URL, APPLICATION_SERVER);
# curl_setopt($ch, CURLOPT_POSTFIELDS, $vars);
# curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
# curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
# $response = curl_exec($ch);
#
# //decode the json encoded response
# $responseVars = decode($response);
#
# $vars['application-id'] = $response['application-id'];
# $key = $response['application-secret-key'];
#
#
# // You must write the code that generates the signature to sign the application
# // request. This is very similar to how other web services handle signatures,
# // so you may be familiar with the process. Here's how to do it:
#
# // 1) Sort the $vars array by key
# $vars = ksort($vars);
#
# // 2) Convert the sorted $vars array to an http query string (eg: var1=abc&var2=def)
# // Note this string should not be prepended with ?, http://, or anything else,
# // it should look like the example string above...
#
# // 3) Concatenate the string from step 2 and $key (string then $key)
#
# // 4) Hash the resulting string from step 3 using SHA256. This is your signature.
# $signature = 'This must be replaced by the code you generate in steps 1,2,3,4)';
#
# // 5) Add the signature to the $vars array as 'sig' (done for you, below)
# $vars['sig'] = $signature;
#
# // Check that the file exists
# if (!file_exists($resumefile)) {
# 	die('ERROR: Cannot find local file '.$resumefile."\n");
# }
#
# // Add the file to upload
# $vars['resume'] = '@'.$resumefile;
#
# // Include this script (we'd like to see your work please!)
# $vars['script'] = '@'.__FILE__;
#
# // Post the data to Pause's server
# print "Submitting application...\n";
# $ch = curl_init();
# curl_setopt($ch, CURLOPT_URL, APPLICATION_SERVER);
# curl_setopt($ch, CURLOPT_POSTFIELDS, $vars);
# curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
# curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
# $response = curl_exec($ch);
#
# // If we got back "OK" then it was submitted successfully.
# // Otherwise it should tell us what went wrong.
# if ($response=='OK') {
# 	print "Resume sent successfully, thank you for applying!\n";
# }
# else {
# 	print "$response\n";
# }
#
#
# Process finished with exit code 0

import os
import time
import hashlib
import requests

# This should point to the resume file you want to submit.
# Note this is a path to the file on your local hard drive,
# not the contents of the file. For best results, use PDF,
# RTF, DOC, DOCX, or TXT.
APPLICATION_SERVER = 'https://jobs.pause.ca/submit.php'

resume_file = 'C:\Resume\SukhbirResume.pdf'

# Your full name
name = 'Sukhbir Singh'

# Your phone number
phone = '6476678741'

# Your email address
email = 'singhsukhbir0911@gmail.com'

# The message we want to send
subject = 'My developer application'

# Any additional notes you wish to include
# Bonus points if you discover the security issue with this script or
# have ideas for improvements and note them here.
notes = ''

# Prepare the payload
vars = {
    'name': name,
    'phone': phone,
    'email': email,
    'subject': subject,
    'notes': notes,
    'time': int(time.time()),
}

response = requests.post(APPLICATION_SERVER, data=vars, verify=False)

# decode the json encoded response
response_vars = response.json()
# print(response_vars)
vars['application-id'] = response_vars['application-id']
key = response_vars['application-secret-key']

# You must write the code that generates the signature to sign the application
# request. This is very similar to how other web services handle signatures,
# so you may be familiar with the process. Here's how to do it:

# 1) Sort the vars dictionary by key
sorted_vars = dict(sorted(vars.items()))

# 2) Convert the sorted vars dictionary to an http query string (eg: var1=abc&var2=def)
# Note this string should not be prepended with ?, http://, or anything else,
# it should look like the example string above...
query_string = '&'.join([f"{k}={v}" for k, v in sorted_vars.items()])

# 3) Concatenate the string from step 2 and key (string then key)
to_sign = query_string + key

# 4) Hash the resulting string from step 3 using SHA256. This is your signature.
signature = hashlib.sha256(to_sign.encode('utf-8')).hexdigest()

# 5) Add the signature to the vars dictionary as 'sig' (done for you, below)
vars['sig'] = signature

# Check that the file exists
if not os.path.exists(resume_file):
    print(f'ERROR: Cannot find local file {resume_file}\n')
    exit()

# Add the file to upload
vars['resume'] = ('resume.pdf', open(resume_file, 'rb'), 'application/pdf')

# Include this script (we'd like to see your work please!)
vars['script'] = ('script.py', open(__file__, 'rb'), 'text/plain')

# Post the data to Pause's server
print("Submitting application...")
response = requests.post(APPLICATION_SERVER, files=vars, verify=False)

# If we got back "OK" then it was submitted successfully.
# Otherwise it should tell us what went wrong.
if response.text == 'OK':
    print("Resume sent successfully, thank you for applying!")
else:
    print(response.text)
