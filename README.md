PyCharm 2024.3.2 - Build #PC-243.23654.177

Atunci cand incerc sa rulez un test individual (de ex: test_SuccessfulLogin) sau intreaga suita de teste imi apare eroarea:
  
  ============================= test session starts =============================
  collecting ... 
  LoginTests.py:None (LoginTests.py)
  C:\Users\User\AppData\Local\Programs\Python\Python312\Lib\unittest\case.py:511: in __hash__
      return hash((type(self), self._testMethodName))
  E   AttributeError: 'LoginTests' object has no attribute '_testMethodName'
  collected 0 items / 1 error

  ============================== 1 error in 0.80s ===============================
  ERROR: found no collectors for C:\Users\User\Desktop\QA_apps\Testing\SauceLabs_UnitTest\TestingFramework\tests\LoginTests.py::LoginTests::test_SuccessfulLogin


  Process finished with exit code 4
