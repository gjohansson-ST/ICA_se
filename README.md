# ICA.se Handla API

#THIS IS NOT WORKING

This integration do use your account credentials.
Insert into configuration.yaml as part of integration installation.

Guide:

```python
 sensor:
   - platform: ica_se
     username: !secret ica_username
     password: !secret ica_password
```
Debug logging (optional)
```python
 logger:
   logs:
     custom_components.ica_se: debug
```
Restart Home Assistant
