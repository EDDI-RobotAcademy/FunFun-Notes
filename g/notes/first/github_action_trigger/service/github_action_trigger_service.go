package service

type GitHubActionTriggerService interface {
	GetTriggers(repoUrl string, token string) ([]string, error)
}
