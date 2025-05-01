package controller

import (
	"first/github_action_trigger/controller/request_form"
	"first/github_action_trigger/service"
	"github.com/gofiber/fiber/v2"
)

type GitHubActionTriggerController struct {
	GitHubActionTriggerService service.GitHubActionTriggerService
}

func NewGitHubActionTriggerController(service service.GitHubActionTriggerService) *GitHubActionTriggerController {
	return &GitHubActionTriggerController{GitHubActionTriggerService: service}
}

func (c *GitHubActionTriggerController) GetTriggers(ctx *fiber.Ctx) error {
	println("controller - GetTriggers() 시작")

	var req request_form.WorkflowTriggerRequestForm
	if err := ctx.BodyParser(&req); err != nil {
		println("controller - BodyParser 오류:", err)
		return ctx.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": "Invalid request"})
	}

	println("controller - 요청 파싱 완료")

	if req.RepoUrl == "" || req.Token == "" {
		println("controller - repoUrl 또는 token이 비어있음")
		return ctx.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": "Missing repoUrl or token"})
	}

	println("controller - repoUrl 및 token 확인 완료")

	triggers, err := c.GitHubActionTriggerService.GetTriggers(req.RepoUrl, req.Token)
	if err != nil {
		println("controller - GetTriggers 오류:", err)
		return ctx.Status(fiber.StatusInternalServerError).JSON(fiber.Map{"error": err.Error()})
	}

	println("controller - 트리거 데이터 가져오기 완료")

	return ctx.JSON(fiber.Map{"triggers": triggers})
}
