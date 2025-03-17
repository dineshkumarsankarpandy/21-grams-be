import openai




def get_llm_response(user_prompt, system_prompt):
        try:
            response = openai.chat.completions.create(
                model="o3-mini-2025-01-31",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
            )
            res = response.choices[0].message.content
            return res
        except Exception as e:
            print(f"Error during OpenAI API call: {e}")
            return None