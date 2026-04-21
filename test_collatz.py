import pytest
from collatz import collatz_sequence, print_result

class TestCollatzSequence:
  """collatz_sequence 関数のテスト群。"""

  def test_starts_with_input(self):
    """数列の先頭が入力値と一致することを確認する。"""
    assert collatz_sequence(6)[0] == 6

  def test_ends_with_one(self):
    """数列の末尾が必ず 1 になることを確認する。"""
    for n in [1, 2, 3, 6, 27, 100]:
      assert collatz_sequence(n)[-1] == 1

  def test_n1_returns_just_one(self):
    """n=1 のとき [1] のみを返すことを確認する。"""
    assert collatz_sequence(1) == [1]

  def test_n2(self):
    """n=2 のとき [2, 1] を返すことを確認する。"""
    assert collatz_sequence(2) == [2, 1]

  def test_n6_known_sequence(self):
    """n=6 の既知の数列と一致することを確認する。"""
    assert collatz_sequence(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]

  def test_n27_steps(self):
    """n=27 のステップ数が 111 であることを確認する。"""
    assert len(collatz_sequence(27)) - 1 == 111

  def test_n27_peak(self):
    """n=27 の最大値が 9232 であることを確認する。"""
    assert max(collatz_sequence(27)) == 9232

  def test_even_rule(self):
    """偶数要素の次が必ず半分になることを確認する。"""
    seq = collatz_sequence(8)
    for i in range(len(seq) - 1):
      if seq[i] % 2 == 0:
        assert seq[i + 1] == seq[i] // 2

  def test_odd_rule(self):
    """奇数要素の次が必ず 3n+1 になることを確認する。"""
    seq = collatz_sequence(27)
    for i in range(len(seq) - 1):
      if seq[i] % 2 != 0:
        assert seq[i + 1] == 3 * seq[i] + 1

  def test_large_number(self):
    """大きな値（1,000,000）でも正しく動作することを確認する。"""
    seq = collatz_sequence(1_000_000)
    assert seq[0] == 1_000_000
    assert seq[-1] == 1

  @pytest.mark.parametrize("n", [1, 2, 3, 4, 5, 10, 27, 100, 871])
  def test_always_reaches_one(self, n):
    """複数の値で数列が必ず 1 に到達することを確認する。"""
    assert collatz_sequence(n)[-1] == 1

class TestPrintResult:
  """print_result 関数のテスト群。"""

  def test_output_contains_start(self, capsys):
    """出力に開始値が含まれることを確認する。"""
    print_result(6)
    out = capsys.readouterr().out
    assert "開始値: 6" in out

  def test_output_contains_steps(self, capsys):
    """出力にステップ数が含まれることを確認する。"""
    print_result(6)
    out = capsys.readouterr().out
    assert "ステップ数: 8" in out

  def test_output_contains_peak(self, capsys):
    """出力に最大値が含まれることを確認する。"""
    print_result(6)
    out = capsys.readouterr().out
    assert "最大値: 16" in out

  def test_output_contains_sequence(self, capsys):
    """出力に数列が含まれることを確認する。"""
    print_result(2)
    out = capsys.readouterr().out
    assert "2 → 1" in out
