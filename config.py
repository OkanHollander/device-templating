import sys
import yaml
import json
import jinja2
from pathlib import Path


def main():
    variables_file = Path(sys.argv[1])
    template_file = Path(sys.argv[2])
    output_file = Path(sys.argv[3])

    # Depending on the file format, use the respective data library
    if variables_file.suffix in [".yml", ".yaml"]:
        with open(variables_file, "r") as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
    elif variables_file.suffix == ".json":
        with open(variables_file, "r") as f:
            data = json.load(f)
    else:
        sys.exit(f"Not supported file format: {variables_file.suffix}")

    # Verify template format
    if template_file.suffix != ".j2":
        sys.exit(f"Template file format not supported: {template_file.suffix}")

    # Get the template data from file
    with open(template_file, "r") as f:
        template_data = f.read()

    # Generate template object
    template = jinja2.Template(template_data)

    # Render the template
    configuration_data = template.render(data)

    # Save the configuration to output file
    with open(output_file, "w") as f:
        f.write(configuration_data)

    print(f"Created File! --> {output_file}")
    # print(configuration_data)
    return


if __name__ == "__main__":
    main()
