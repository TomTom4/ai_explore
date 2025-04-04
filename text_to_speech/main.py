from deepgram import DeepgramClient, SpeakOptions
from dotenv import load_dotenv

load_dotenv()

SPEAK_TEXT = {"text": "Hello dear! My name is Asteria. How can I help you today?"}
filename = "test.mp3"


def main():
    try:
        # STEP 1 Create a Deepgram client using the API key from environment variables
        deepgram = DeepgramClient()

        # STEP 2 Call the save method on the speak property
        options = SpeakOptions(
            model="aura-asteria-en",
        )

        response = deepgram.speak.rest.v("1").save(filename, SPEAK_TEXT, options)
        print(response.to_json(indent=4))

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
