import pytest


@pytest.marker.liu
def test_01(self):
    print("test01")


def test_02(self):
    print("test02")


def test_03(self):
    print("test03")


if __name__ == '__main__':
   pytest.main("-vs",)