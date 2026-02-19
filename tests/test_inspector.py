from datadoctor.inspector import inspect_file

def test_inspect_basic_csv(tmp_path):
    # Create a small CSV file
    file = tmp_path / "sample.csv"
    file.write_text("a,b,c\n1,2,3\n4,5,6\n")

    result = inspect_file(str(file))

    assert "structure" in result
    assert "score" in result
    assert result["structure"]["total_rows"] == 2
    assert result["structure"]["expected_columns"] == 3
