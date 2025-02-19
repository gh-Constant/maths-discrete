import json

def convert_to_ts(data, variable_name="sednaData"):
    """
    Converts a JSON-like data structure into a TypeScript const declaration
    that follows the provided SednaNode type. Handles a list of SednaNode objects.

    Args:
        data: A dictionary or a list of dictionaries representing the hierarchical data.
        variable_name: The name of the TypeScript constant to create.

    Returns:
        A string containing the TypeScript code.
    """

    def process_node(node, indent_level=1):
        """Recursively converts a node to TypeScript format with indentation."""
        indent = "    " * indent_level  # 4 spaces per indent level
        subpages = node.get("subpages", [])
        subpages_ts = ",\n".join([process_node(subpage, indent_level + 1) for subpage in subpages])
        if subpages_ts:
            subpages_ts = f"[\n{indent}{subpages_ts}\n{indent[:-4]}]" # indent[:-4] get rid of an extra tab
        else:
            subpages_ts = "[]"

        return f"""{indent[:-4]}{{
{indent}name: "{node["name"]}",
{indent}url: "{node["url"]}",
{indent}subpages: {subpages_ts}
{indent[:-4]}}}""" # indent[:-4] get rid of an extra tab

    # Check if the input is a list or a single object
    if isinstance(data, list):
        # Process each item in the list
        nodes_ts = ",\n".join([process_node(node) for node in data])
        root_node_ts = f"[\n{nodes_ts}\n]"
        typescript_type = "SednaNode[]"
    else:
        # Process the single object
        root_node_ts = process_node(data)
        typescript_type = "SednaNode"

    typescript_code = f"""const {variable_name}: {typescript_type} = {root_node_ts};\n"""
    return typescript_code


# Example Usage:  Read from a JSON file and write the converted Typescript code to another file.
input_filename = "input.json"  # Replace with your input JSON filename
output_filename = "output.ts" # Replace with your desired output TypeScript filename


try:
    with open(input_filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    typescript_code = convert_to_ts(data)

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(typescript_code)

    print(f"Conversion successful.  TypeScript code written to {output_filename}")

except FileNotFoundError:
    print(f"Error: Input file '{input_filename}' not found.")
except json.JSONDecodeError:
    print(f"Error: Invalid JSON in file '{input_filename}'.")
except Exception as e:
    print(f"An error occurred: {e}")