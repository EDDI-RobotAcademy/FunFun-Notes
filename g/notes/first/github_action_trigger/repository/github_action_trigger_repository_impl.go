package repository

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strings"
)

type GitHubActionTriggerRepositoryImpl struct{}

// NewGitHubActionTriggerRepositoryImpl 생성자 함수
func NewGitHubActionTriggerRepositoryImpl() GitHubActionTriggerRepository {
	return &GitHubActionTriggerRepositoryImpl{}
}

func (r *GitHubActionTriggerRepositoryImpl) FetchTriggers(repoUrl string, token string) ([]string, error) {
	owner, repo, err := parseRepoURL(repoUrl)
	if err != nil {
		return nil, fmt.Errorf("invalid repo URL: %w", err)
	}

	apiUrl := fmt.Sprintf("https://api.github.com/repos/%s/%s/actions/workflows", owner, repo)

	req, err := http.NewRequest("GET", apiUrl, nil)
	if err != nil {
		return nil, err
	}
	req.Header.Set("Authorization", "Bearer "+token)
	req.Header.Set("Accept", "application/vnd.github+json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	if resp.StatusCode != 200 {
		return nil, fmt.Errorf("GitHub API returned status %d", resp.StatusCode)
	}

	var result struct {
		Workflows []struct {
			Name     string `json:"name"`
			FileName string `json:"path"`
		} `json:"workflows"`
	}

	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return nil, err
	}

	var triggers []string
	for _, wf := range result.Workflows {
		triggers = append(triggers, wf.FileName)
	}

	return triggers, nil
}

// parseRepoURL extracts owner and repo from full repo URL
func parseRepoURL(repoUrl string) (string, string, error) {
	// Example input: https://github.com/owner/repo
	trimmed := strings.TrimPrefix(repoUrl, "https://github.com/")
	parts := strings.Split(trimmed, "/")
	if len(parts) < 2 {
		return "", "", fmt.Errorf("invalid repo URL")
	}
	return parts[0], parts[1], nil
}
