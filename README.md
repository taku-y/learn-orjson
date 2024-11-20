# learn-orjson
このリポジトリは[`orjson`](https://pypi.org/project/orjson/)を用いてJSONを介してRustで生成したオブジェクトをPythonで復元できるかどうかを検証するためのプログラムが含まれます。

## 動作確認

### Serialization
```bash
cargo run
```

```bash
cat data.json
```

In `data.json`:
```
{
  "name": "test",
  "x": [
    {
      "data": [
        1.0,
        2.0,
        3.0
      ],
      "dim": [
        3
      ],
      "v": 1
    }
  ]
}
```

### Deserialization
```bash
uv sync
```

Output:
```
Data(name='test', x=[array([1., 2., 3.])])
```
