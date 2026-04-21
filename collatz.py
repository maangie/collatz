import sys

def collatz_sequence(n: int) -> list[int]:
  """コラッツ数列を返す。n から始まり 1 に到達するまでの全要素を含むリスト。"""
  seq = [n]
  while n != 1:
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    seq.append(n)
  return seq

def print_result(n: int) -> None:
  """n のコラッツ数列の開始値・ステップ数・最大値・数列を標準出力に表示する。"""
  seq = collatz_sequence(n)
  steps = len(seq) - 1
  peak = max(seq)

  print(f"開始値: {n}")
  print(f"ステップ数: {steps}")
  print(f"最大値: {peak}")
  print(f"数列: {' → '.join(map(str, seq))}")

def main() -> None:
  """コマンドライン引数または標準入力から正の整数を受け取り、コラッツ数列の結果を表示する。"""
  args = sys.argv[1:]

  if not args:
    try:
      raw = input("正の整数を入力してください: ").strip()
    except (EOFError, KeyboardInterrupt):
      print()
      return
    args = [raw]

  for arg in args:
    try:
      n = int(arg)
      if n <= 0:
        print(f"エラー: '{arg}' は正の整数ではありません", file=sys.stderr)
        continue
    except ValueError:
      print(f"エラー: '{arg}' は整数ではありません", file=sys.stderr)
      continue

    if len(args) > 1:
      print(f"--- {n} ---")
    print_result(n)
    if len(args) > 1:
      print()

if __name__ == "__main__":
  main()
