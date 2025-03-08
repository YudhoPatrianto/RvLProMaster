import io
import sys
import textwrap

class PythonTerminal:
    @staticmethod
    async def Run(command_in):
        corrected_command_indent = textwrap.dedent(command_in)
        output_command = io.StringIO()
        original_stdout = sys.stdout
        original_stderr = sys.stderr
        sys.stdout = output_command
        sys.stderr = output_command
        error_message = ""
        try:
            exec_code = f'async def __exec():\n{textwrap.indent(corrected_command_indent, "    ")}'
            exec_locals = {}
            exec(exec_code, globals(), exec_locals)
            await exec_locals['__exec']()
        except Exception as e:
            error_message = str(e)
        finally:
            sys.stdout = original_stdout
            sys.stderr = original_stderr        
        return output_command.getvalue() + ("\n" + error_message if error_message else "")
    
PythonTerminal = PythonTerminal()
