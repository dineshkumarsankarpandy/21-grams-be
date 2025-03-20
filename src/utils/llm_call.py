import openai




def get_llm_response(user_prompt:str, system_prompt:str, response_format):
        try:
            response = openai.beta.chat.completions.parse(
                model="o3-mini-2025-01-31",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                response_format= response_format
            )
            res = response.choices[0].message.parsed
            return res
        except Exception as e:
            print(f"Error during OpenAI API call: {e}")
            return None