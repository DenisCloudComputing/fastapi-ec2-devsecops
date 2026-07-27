# Déploiement d'une API FastAPI sur Amazon EC2

> **Ce projet est un portfolio DevSecOps complet.**  
> Il documente, étape par étape, comment déployer une application Python  
> sur le cloud AWS — de zéro jusqu'à une architecture d'entreprise.

---

## Pourquoi ce projet existe

Déployer une application sur le cloud, ça fait peur au début.  
Des mots comme "EC2", "SSH", "reverse proxy", "CI/CD" semblent compliqués.  
Ce projet prouve que **non, ce n'est pas sorcier** — si on y va étape par étape.

---

## Ce que tu vas trouver ici

| Niveau | Thème | Technologies |
|--------|-------|-------------|
| 1 — Fondations | Déploiement manuel | EC2, SSH, FastAPI, systemd |
| 2 — Industrialisation | Sécurité et domaine | Nginx, HTTPS, Route 53 |
| 3 — Robustesse | Haute disponibilité | RDS, Load Balancer, S3 |
| 4 — Automatisation | CI/CD et Docker | Terraform, GitHub Actions |
| 5 — Enterprise | Orchestration | ECS, Kubernetes, WAF |

---

## Architecture cible

```text
Utilisateur (toi, depuis ton navigateur)
        ↓
   Internet
        ↓
  DNS / Route 53  ← annuaire téléphonique d'Internet
        ↓
     Nginx        ← portier / réceptionniste
        ↓
FastAPI/Uvicorn   ← le cerveau, ton application Python
        ↓
 Base de données ou services AWS