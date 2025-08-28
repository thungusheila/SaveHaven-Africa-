from flask import Blueprint, request, jsonify
from models import Report
from database import db
from utils import compute_hotspots

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/health", methods=["GET"])
def health():
    return jsonify({"ok": True})

@bp.route("/reports", methods=["POST"])
def create_report():
    data = request.get_json() or {}
    category = data.get("category")
    description = data.get("description")
    location = data.get("location") or {}
    lat = location.get("lat") or data.get("lat")
    lng = location.get("lng") or data.get("lng")
    if not category or not description or lat is None or lng is None:
        return jsonify({"error": "Missing required fields"}), 400
    rpt = Report(
        category=category,
        description=description,
        lat=float(lat),
        lng=float(lng),
        address=location.get("address") or data.get("address"),
        anonymous=bool(data.get("anonymous", True)),
        contact=data.get("contact")
    )
    db.session.add(rpt)
    db.session.commit()
    return jsonify(rpt.to_dict()), 201

@bp.route("/reports", methods=["GET"])
def list_reports():
    limit = min(int(request.args.get("limit", 50)), 500)
    reports = Report.query.order_by(Report.created_at.desc()).limit(limit).all()
    return jsonify([r.to_dict() for r in reports])

@bp.route("/stats/hotspots", methods=["GET"])
def hotspots():
    precision = min(max(int(request.args.get("precision", 2)), 0), 6)
    data = compute_hotspots(precision=precision, limit=100)
    return jsonify(data)
