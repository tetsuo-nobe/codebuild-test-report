# AWS CodeBuild のテストレポートのサンプル

- テスト対象のアプリケーション: FizzBuzz.py 
    - fizzbuzz 関数 の要件
        - 3 の倍数なら 'Fizz' を返す
        - 5 の倍数なら 'Buzz' を返す
        - 3 と 5 の公倍数なら 'FizzBuzz' を返す
- テスト: test_FizzBuzz.py
    - pytest を使用してテスト
        -  (テストレポートの出力を容易にするため標準の unittest パッケージではなく pytest を使っている）
- buildspec.yaml
    - reports セクションでテストレポートを指定
