import pytest
from collatz import collatz_sequence, print_result


class TestCollatzSequence:
  def test_starts_with_input(self):
    assert collatz_sequence(6)[0] == 6

  def test_ends_with_one(self):
    for n in [1, 2, 3, 6, 27, 100]:
      assert collatz_sequence(n)[-1] == 1

  def test_n1_returns_just_one(self):
    assert collatz_sequence(1) == [1]

  def test_n2(self):
    assert collatz_sequence(2) == [2, 1]

  def test_n6_known_sequence(self):
    assert collatz_sequence(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]

  def test_n27_steps(self):
    assert len(collatz_sequence(27)) - 1 == 111

  def test_n27_peak(self):
    assert max(collatz_sequence(27)) == 9232

  def test_even_rule(self):
    # 偶数は必ず半分になる
    seq = collatz_sequence(8)
    for i in range(len(seq) - 1):
      if seq[i] % 2 == 0:
        assert seq[i + 1] == seq[i] // 2

  def test_odd_rule(self):
    # 奇数は 3n+1 になる
    seq = collatz_sequence(27)
    for i in range(len(seq) - 1):
      if seq[i] % 2 != 0:
        assert seq[i + 1] == 3 * seq[i] + 1

  def test_large_number(self):
    seq = collatz_sequence(1_000_000)
    assert seq[0] == 1_000_000
    assert seq[-1] == 1

  @pytest.mark.parametrize("n", [1, 2, 3, 4, 5, 10, 27, 100, 871])
  def test_always_reaches_one(self, n):
    assert collatz_sequence(n)[-1] == 1


class TestPrintResult:
  def test_output_contains_start(self, capsys):
    print_result(6)
    out = capsys.readouterr().out
    assert "開始値: 6" in out

  def test_output_contains_steps(self, capsys):
    print_result(6)
    out = capsys.readouterr().out
    assert "ステップ数: 8" in out

  def test_output_contains_peak(self, capsys):
    print_result(6)
    out = capsys.readouterr().out
    assert "最大値: 16" in out

  def test_output_contains_sequence(self, capsys):
    print_result(2)
    out = capsys.readouterr().out
    assert "2 → 1" in out
