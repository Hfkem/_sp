#  作業一：
  作業 dowhile全由AI輔助完成 (vscode內codeinum輔助工具)，其餘為老師原檔
  void DOWHILE(){
  int dowhileBegin = nextLabel();
  int dowhileEnd = nextLabel();
  emit("(L%d)\n", dowhileBegin);
  skip("do");
  skip("{");
  STMT();
  skip("}");
  skip("while");
  skip("(");
  int e = E();
  emit("if not T%d goto L%d\n", e, dowhileEnd);
  skip(")");
  skip(";");
  emit("goto L%d\n", dowhileBegin);
  emit("(L%d)\n", dowhileEnd);
}
