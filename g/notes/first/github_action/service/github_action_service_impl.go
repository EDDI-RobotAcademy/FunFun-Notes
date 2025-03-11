package service

import (
	"errors"
	"first/github_action/entity"
	"first/github_action/repository"
)

// GitHubActionServiceImpl은 GitHubActionService 인터페이스를 구현하는 구조체입니다.
type GitHubActionServiceImpl struct {
	GitHubRepo repository.GitHubActionRepository
}

// NewGitHubActionServiceImpl 생성자 함수
func NewGitHubActionServiceImpl(gitHubRepo repository.GitHubActionRepository) GitHubActionService {
	return &GitHubActionServiceImpl{GitHubRepo: gitHubRepo}
}

// GetWorkflowRuns 구현
func (s *GitHubActionServiceImpl) GetWorkflowRuns(repoUrl string, token string) ([]entity.WorkflowRun, error) {
	// GitHub API와 상호작용하여 워크플로우 실행 정보 가져오기 (실제 API 호출 로직은 여기서 구현)
	return []entity.WorkflowRun{}, nil
}

// SaveWorkflowRuns 구현
func (s *GitHubActionServiceImpl) SaveWorkflowRuns(workflows []entity.WorkflowRun) error {
	return s.GitHubRepo.SaveWorkflowRuns(workflows)
}

// GetWorkflowRunByID 구현
func (s *GitHubActionServiceImpl) GetWorkflowRunByID(id uint) (*entity.WorkflowRun, error) {
	workflowRun, err := s.GitHubRepo.GetWorkflowRunByID(id)
	if err != nil {
		return nil, err
	}
	if workflowRun == nil {
		return nil, errors.New("workflow run not found")
	}
	return workflowRun, nil
}

// DeleteWorkflowRun 구현
func (s *GitHubActionServiceImpl) DeleteWorkflowRun(id uint) error {
	workflowRun, err := s.GitHubRepo.GetWorkflowRunByID(id)
	if err != nil {
		return err
	}
	if workflowRun == nil {
		return errors.New("workflow run not found")
	}
	return s.GitHubRepo.DeleteWorkflowRun(id)
}
