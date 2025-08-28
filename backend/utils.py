from models import Report
from database import db
from sqlalchemy import func

def compute_hotspots(precision=2, limit=100):
    """
    Simple binning: round lat/lng to given decimal precision and count.
    """
    # Uses raw SQL approach for SQLite (works for simple MVP)
    bin_expr_lat = func.round(Report.lat, precision)
    bin_expr_lng = func.round(Report.lng, precision)
    q = db.session.query(bin_expr_lat.label('lat'), bin_expr_lng.label('lng'), func.count(Report.id).label('count')) \
        .group_by(bin_expr_lat, bin_expr_lng) \
        .order_by(func.count(Report.id).desc()) \
        .limit(limit)
    return [{"lat": row.lat, "lng": row.lng, "count": row.count} for row in q]
