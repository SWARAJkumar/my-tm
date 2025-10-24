import os
import pytest
import requests

# ✅ Base URL for the deployed modelmgmtService
# Example: http://tm.traininghost.svc.cluster.local:80
BASE_URL = os.getenv(
    "TM_BASE_URL",
    "http://localhost:32002"
)


@pytest.mark.regression
def test_get_all_models():
    """✅ Validate GET /ai-ml-model-training/v1/featureGroup returns 200 and valid JSON."""
    url = f"{BASE_URL}/ai-ml-model-training/v1/featureGroup"
    print(f"Fetching all FG from: {url}")
    resp = requests.get(url, timeout=10)-
    assert resp.status_code == 200, f"Expected 200 OK, got {resp.status_code}"
    try:
        data = resp.json()
    except Exception as e:
        pytest.fail(f"Response is not valid JSON: {e}")
    assert isinstance(data, (list, dict)), "Expected response type list or dict"
    print("Model list API response validated.")
