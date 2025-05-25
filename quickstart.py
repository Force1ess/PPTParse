from copy import deepcopy
from dataclasses import asdict

from dacite import from_dict

from pptparse import Config, Presentation

# Load a presentation
config = Config("/tmp")
prs = Presentation.from_file("test.pptx", config)


# Parse the presentation to dict, noting you must use `deepcopy` to avoid deepcopy `shape` objects
prs_attrs = asdict(deepcopy(prs))
print(prs_attrs)

# Convert attr dict to a `Presentation` object
prs: Presentation = from_dict(data_class=Presentation, data=prs_attrs)
prs.save("test_output.pptx")
