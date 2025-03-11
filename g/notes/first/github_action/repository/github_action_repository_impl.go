package repository

import (
	"encoding/json"
	"first/github_action/entity"
	"fmt"
	"net/http"

	"github.com/pkg/errors"

	"gorm.io/gorm"
)

// GitHubActionRepositoryImpl은 GitHubActionRepository 인터페이스를 구현하는 구조체입니다.
type GitHubActionRepositoryImpl struct {
	DB *gorm.DB
}

// NewGitHubActionRepositoryImpl 생성자 함수
func NewGitHubActionRepositoryImpl(db *gorm.DB) GitHubActionRepository {
	return &GitHubActionRepositoryImpl{DB: db}
}

// GetWorkflowRuns 구현
// GitHub API와 상호작용하여 워크플로우 실행 정보를 가져옵니다.
func (r *GitHubActionRepositoryImpl) GetWorkflowRuns(repoUrl string, token string) ([]entity.WorkflowRun, error) {
	// GitHub API 엔드포인트 구성
	// repoUrl은 GitHub 레포지토리 URL 형식이어야 하므로, 예시로 'owner/repo' 형식을 사용합니다.
	apiURL := fmt.Sprintf("https://api.github.com/repos/%s/actions/runs", repoUrl)

	// 요청을 위한 HTTP 클라이언트 설정
	client := &http.Client{}
	req, err := http.NewRequest("GET", apiURL, nil)
	if err != nil {
		return nil, errors.Wrap(err, "failed to create request")
	}

	// 인증을 위한 Authorization 헤더 추가
	req.Header.Set("Authorization", "token "+token)
	req.Header.Set("Accept", "application/vnd.github.v3+json")

	// 요청 보내기
	resp, err := client.Do(req)
	if err != nil {
		return nil, errors.Wrap(err, "failed to send request")
	}
	defer resp.Body.Close()

	// 응답이 성공적이지 않으면 오류 반환
	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("failed to get workflow runs, status code: %d", resp.StatusCode)
	}

	// 응답 본문을 구조체로 변환
	var result struct {
		WorkflowRuns []entity.WorkflowRun `json:"workflow_runs"`
	}

	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return nil, errors.Wrap(err, "failed to decode response body")
	}

	return result.WorkflowRuns, nil
}

// SaveWorkflowRuns 구현
// 워크플로우 실행 정보를 데이터베이스에 저장합니다.
func (r *GitHubActionRepositoryImpl) SaveWorkflowRuns(workflows []entity.WorkflowRun) error {
	return r.DB.Create(&workflows).Error
}

// GetWorkflowRunByID 구현
// 특정 워크플로우 실행 정보를 ID로 가져옵니다.
func (r *GitHubActionRepositoryImpl) GetWorkflowRunByID(id uint) (*entity.WorkflowRun, error) {
	var workflowRun entity.WorkflowRun
	if err := r.DB.First(&workflowRun, id).Error; err != nil {
		return nil, err
	}
	return &workflowRun, nil
}

// DeleteWorkflowRun 구현
// 특정 워크플로우 실행 정보를 데이터베이스에서 삭제합니다.
func (r *GitHubActionRepositoryImpl) DeleteWorkflowRun(id uint) error {
	var workflowRun entity.WorkflowRun
	if err := r.DB.First(&workflowRun, id).Error; err != nil {
		return err
	}
	return r.DB.Delete(&workflowRun).Error
}
