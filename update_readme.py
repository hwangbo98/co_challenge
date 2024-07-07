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
        for i, line in enumerate(readme_content):
            if line.startswith('| 날짜       | 문제       |'):
                readme_content.insert(i + 2, new_entry)
                break

        with open(readme_path, 'w') as file:
            file.writelines(readme_content)
        break