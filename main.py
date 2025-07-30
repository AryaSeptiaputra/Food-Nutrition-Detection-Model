from src.pipeline.buildPipeline import BuildPipeline

def main():
    pipeline = BuildPipeline()
    while True:
        user_prompt = input("\nMasukkan pertanyaan tentang makanan (atau ketik 'exit' untuk keluar): ")
        if user_prompt.lower() == "exit":
            print("\nTerima kasih telah menggunakan asisten gizi virtual.")
            break
        response = pipeline.pipeline_prompt_only(user_prompt)
        print("\n=== Jawaban ===")
        print(response)

if __name__ == "__main__":
    main()