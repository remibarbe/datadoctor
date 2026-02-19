from typer.testing import CliRunner
from datadoctor.cli import app

runner = CliRunner()

def test_cli_json_output(tmp_path):
    file = tmp_path / "sample.csv"
    file.write_text("a,b\n1,2\n")

    result = runner.invoke(app, [str(file), "--json"])

    assert result.exit_code == 0
    assert "structure" in result.stdout
    assert "score" in result.stdout
