import os
import re
from datetime import datetime
from github import Github

# 환경 변수에서 GitHub 토큰과 리포지토리 이름 가져오기
github_token = os.getenv('MY_GITHUB_TOKEN')
repo_name = os.getenv('GITHUB_REPOSITORY')

# GitHub API 클라이언트 설정
g = Github(github_token)
repo = g.get_repo(repo_name)

# 최신 커밋 가져오기
commits = repo.get_commits()
latest_commit = commits[0]
files = latest_commit.files

# README 파일 업데이트
readme_path = 'README.md'
with open(readme_path, 'r') as file:
    readme_content = file.readlines()

# 날짜 가져오기
today = datetime.today().strftime('%Y-%m-%d')

# 커밋 메시지에서 문제 이름 파싱 (예: "Add problem: 문제 이름")
commit_message = latest_commit.commit.message
pattern = re.compile(r'Add problem: (.+)')
match = pattern.search(commit_message)

if match:
    problem_name = match.group(1)

    # 문제 링크 생성
    base_url = f"https://github.com/{repo_name}/blob/main/"
    for file in files:
        file_path = file.filename
        problem_link = base_url + file_path

        # README에 새 항목 추가
        new_entry = f"| {today} | [{problem_name}]({problem_link}) |\n"
        if new_entry not in readme_content:  # 이미 추가된 항목인지 확인
            # 가장 맨 밑에 위치한 날짜 문제 항목의 아래에 추가
            for i in range(len(readme_content) - 1, -1, -1):
                if readme_content[i].startswith('|') and '|' in readme_content[i]:
                    readme_content.insert(i + 1, new_entry)
                    break

            with open(readme_path, 'w') as file:
                file.writelines(readme_content)
            break

# 추가된 변경 사항이 없을 경우 "Nothing to commit" 메시지 출력
if new_entry in readme_content:
    print("Nothing to commit")
else:
    print("Updated README with new problem")