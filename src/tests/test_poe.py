# test_poe.py

import allure
import pytest


@allure.title("poe")
@pytest.mark.repeat(1)
def test_poe_all(request, serial_env, telnet_env):
    from ..command.usecases.RT_PoE5 import run as on_RT_PoE5
    from ..command.usecases.Poe import run as get_dut_Used_w
    from ..command.usecases.PE6108A import run as reboot_dut
    from ..command.usecases.RT_PoE5 import run2 as get_RT_PoE5_Used_w
    from ..command.usecases.RT_PoE5 import run3 as off_RT_PoE5

    # 重開DUT
    reboot_dut(telnet_env)
    # 開啟RT_PoE5
    on_RT_PoE5(serial_env)
    # 讀取DUT CLI poe Used(W)
    result1 = get_dut_Used_w(serial_env)
    # 讀取RT_PoE5 Used(W)
    result2 = get_RT_PoE5_Used_w(serial_env)
    allure.attach(result1, name=f"供電測試結果1", attachment_type=allure.attachment_type.TEXT)
    allure.attach(result2, name=f"吃電測試結果2", attachment_type=allure.attachment_type.TEXT)
    used_w = float(result1.split()[-1])
    assert "2W" in result2
    assert 2.0 <= used_w <= 2.1

    # 需要 web 測試時再初始化 fixture
    poe_status_page = request.getfixturevalue("poe_status_page")
    result = poe_status_page.get_poe_status_Used_text()
    allure.attach("Used(W):" + result, name=f"web測試結果3", attachment_type=allure.attachment_type.TEXT)
    value = float(result)
    assert 2.0 <= value <= 2.1
    # 關閉RT_PoE5
    off_RT_PoE5(serial_env)
