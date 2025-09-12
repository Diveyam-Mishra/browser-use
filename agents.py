import asyncio
from typing import cast

# from browser_use.llm import ChatOllama
from dotenv import load_dotenv

from browser_use import Agent
from browser_use.browser.profile import BrowserProfile
from browser_use.llm import ChatOpenAI
from browser_use.tools.service import Tools

load_dotenv()

intial_actions = [
	{
		'go_to_url': {
			'url': 'https://crm4ce--idx.sandbox.my.salesforce.com/',
			'new_tab': False,
		}
	},
	{'wait': {'seconds': 10}},
	{'input_text': {'index': 1, 'text': 'dmishra@cybersolve.com'}},
	{'input_text': {'index': 3, 'text': 'Divey@m02'}},
	{'click_element_by_index': {'index': 4}},
	{'wait': {'seconds': 5}},
	{
		'go_to_url': {
			'url': 'https://crm4ce--idx.sandbox.my.salesforce-setup.com/lightning/setup/ManageUsers/page?address=%2F005%2Fe%3FretURL%3D%252F005%253FisUserEntityOverride%253D1%2526retURL%253D%25252Fsetup%25252Fhome%2526appLayout%253Dsetup%2526tour%253D%2526isdtp%253Dp1%2526sfdcIFrameOrigin%253Dhttps%25253A%25252F%25252Fcrm4ce--idx.sandbox.my.salesforce-setup.com%2526sfdcIFrameHost%253Dweb%2526nonce%253D23000d5455766ce3e6005e1e39da6c88a007569a1039179a4547731ce4265b81%2526ltn_app_id%253D%2526clc%253D1%26isUserEntityOverride%3D1',
			'new_tab': False,
		}
	},
	{'wait': {'seconds': 10}},
	{'input_text': {'index': 91, 'text': 'useR'}},
	{'input_text': {'index': 97, 'text': '223423x3r11123aab'}},
	{'input_text': {'index': 106, 'text': 'useR2234aa@exambple.com'}},
	{'click_element_by_index': {'index': 109}},
	{'select_dropdown_option': {'index': 95, 'text': 'EVP Global Business Managing Partner'}},
	{'select_dropdown_option': {'index': 98, 'text': 'Identity'}},
	{'select_dropdown_option': {'index': 99, 'text': 'Identity'}},
]

llm = ChatOpenAI(model='gpt-5')
browser_profile = BrowserProfile(
	#     headless=False,
	#     keep_alive=False,
	#     wait_for_network_idle_page_load_time=3.0,
	#     viewport={"width": 1280, "height": 1100},
	#     args=["-no-sandbox", "--disable-dev-shm-usage", "--disable-gpu"],
	#     highlight_elements=False,
	#     viewport_expansion=-1,
	#     user_data_dir="~/.config/browseruse/profiles/default",
	#     browser_binary_path=Path("/usr/bin/google-chrome"),  # or "/usr/bin/chromium-browser"
	#     disable_security=True
	#
	headless=False,
	keep_alive=True,
	wait_for_network_idle_page_load_time=3.0,
	# viewport={"width": 1280, "height": 1100},
	user_data_dir=None,
	# browser_binary_path=Path(r"C:/Program Files/Google/Chrome/Application/chrome.exe"),  # Adjust path as needed
	highlight_elements=True,
	disable_security=True,
)
# llm = ChatOllama(model='hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q2_K' ,host='http://localhost:11434')
# sensitive_data = {'login_email': 'dmishra@cybersolve.com', 'login_password': 'Divey@m02'}
# sensitive_data = {'login': "admin", 'login_password': 'MZ%uIN5-h8ke'}
tools = Tools()


async def main():
	agent = Agent(
		# initial_actions=intial_actions,
		# sensitive_data=cast(dict[str, str | dict[str, str]], sensitive_data),
		max_actions_per_step=10,
		use_vision=True,
		calculate_cost=True,
		# browser_profile=browser_profile,
		task=(
			"""
             YOur Job is to https://www.youtube.com/watch?v=H1Wbu_AF2e4&list=RDH1Wbu_AF2e4&start_radio=1 tell me the sentiments of people in the top comments section of this video.
			 Then write a single line on https://onlinenotepad.org/notepad
			"""
		),
		llm=llm,
		workflow_record=True,
		workflow_trace_name='Testing',
		workflow_file='workflows.jsonl',
		workflow_replay_first=False,
	)

	# Optional: mark a logical phase so recorded steps get grouped in a sub-task
	result = await agent.run()
	print(result)


asyncio.run(main())
