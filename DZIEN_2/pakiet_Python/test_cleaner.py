from textutils.cleaner import clean_text

def test_clean_text():
    assert clean_text("Hello, World!") == "hello world"
