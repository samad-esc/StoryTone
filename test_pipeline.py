from pipeline import StoryPipeline

pipeline = StoryPipeline()

story = """
She was extremely happy to see him after so many years. 
The room felt empty and silent. 
Fear crept in as the lights went out. 
But hope returned when the door opened again.
"""

output = pipeline.process_story(story)

print("Final audio generated at:", output)
