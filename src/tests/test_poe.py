# test_poe.py

import allure
import pytest


@allure.title("poe")
@pytest.mark.repeat(1)
def test_poe_all(request, serial_env, telnet_env):
    # 先執行 serial/poe 測試
    from ..command.usecases.RT_PoE5 import run
    from ..command.usecases.Poe import run as run2
    from ..command.usecases.PE6108A import run as run3
    #重開DUT
    #run3(telnet_env)
    #讀取DUT CLI poe Used(W)
    result2 = run2(serial_env)
    #開啟RT_PoE5
    result1 = run(serial_env)
    allure.attach(result1, name=f"吃電測試結果1", attachment_type=allure.attachment_type.TEXT)
    allure.attach(result2, name=f"供電測試結果2", attachment_type=allure.attachment_type.TEXT)
    used_w = float(result2.split()[-1])
    assert "2W" in result1
    assert 2.0 <= used_w <= 2.1

    # 需要 web 測試時再初始化 fixture
    poe_status_page = request.getfixturevalue("poe_status_page")
    result = poe_status_page.get_poe_status_Used_text()
    allure.attach(result, name=f"web測試結果3", attachment_type=allure.attachment_type.TEXT)
    value = float(result)
    assert 2.0 <= value <= 2.1
